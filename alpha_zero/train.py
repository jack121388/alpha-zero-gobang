# -*- coding: utf-8 -*-
'''
帮我用写一个Train类，用来执行AI训练，基本原理是调用 ai 进行多次对局，并把对局结果保存到文件中，然后用这些数据训练Net，实现如下方法：
- __init__： 初始化方法，传入这几个参数，board 是Board实例，ai 是要执行对局的AI，net 是神经网络, iterations 是要执行多少轮训练，iteration_epochs 是每一轮训练中执行多少次对局，load_checkpoint 是否要加载之前的checkpoint
- start: 启动训练，执行 self.iterations 轮训练，每一轮执行 self.iteration_epochs 次对局，每一轮结束后，保存训练数据，用数据训练神经网络，然后保存checkpoint
其中的ai和PureMCTS接口是一样的，有一个 train 方法进行训练
'''

import pickle
import numpy as np
import os
from tqdm import tqdm
from random import shuffle
from alpha_zero.players import MCTSPlayer
from alpha_zero.arena import Arena
from copy import deepcopy

checkpoint_dir = 'checkpoint'
checkpoint_file = os.path.join(checkpoint_dir, 'best_checkpoint.h5')
tmp_checkpoint_file = os.path.join(checkpoint_dir, 'tmp_checkpoint.h5')
data_file = os.path.join(checkpoint_dir, 'train_data.pkl')

class Train:
  def __init__(self, board, ai, net, prev_net, iterations=100, iteration_epochs=100, train_data_limit=2000, load_checkpoint=False, temp_threshold=20):
    self.board = board
    self.ai = ai
    self.net = net
    self.prev_net = prev_net
    self.iterations = iterations
    self.iteration_epochs = iteration_epochs
    self.data_limit = train_data_limit
    self.load_checkpoint = load_checkpoint
    self.temp_threshold = temp_threshold
    self.train_data_history = []

  def start(self):
    # 创建文件夹
    if not os.path.exists(checkpoint_dir):
      print("create checkpoint directory: {}".format(checkpoint_dir))
      os.mkdir(checkpoint_dir)
    if self.load_checkpoint:
      print('loading checkpoint...')
      self.net.load(checkpoint_file)
      print('checkpoint loaded success')
      with open(data_file, 'rb') as f:
        print('loading train_data...')
        self.train_data_history= pickle.load(f)
      print('train_data loaded success, total length :', len(self.train_data_history))

    for iteration in range(self.iterations):
      print(f"Starting iteration {iteration + 1}/{self.iterations}...")
      iteration_data = self._run_iteration()

      # make new train data
      train_data = deepcopy(self.train_data_history)

      train_data.extend(iteration_data)
      print('train_data length:', len(train_data))

      # If the training data exceeds the limit, remove the oldest data.
      if len(train_data) > self.data_limit:
        del train_data[:len(self.train_data) - self.data_limit]
        print('train_data length after remove out of limit:', len(train_data))

      print("Training...")

      # shuffle the data before training
      shuffled_train_data = deepcopy(train_data)
      shuffle(shuffled_train_data)

      X, y_v, y_p = zip(*shuffled_train_data)

      self.net.save(tmp_checkpoint_file)
      self.prev_net.load(tmp_checkpoint_file)

      # do the training
      self.net.train(np.array(X), np.array(y_v), np.array(y_p))

      print("Pitting against previous version...")
      prev_ai = MCTSPlayer(board=self.board, net=self.prev_net, simulation_num=self.ai.simulation_num)
      current_ai = MCTSPlayer(board=self.board, net=self.net, simulation_num=self.ai.simulation_num)

      area = Arena(board=self.board, ai1=prev_ai, ai2=current_ai, random_opening=True)
      wins, fails, draws = area.start(match_count=10, verbose=False)

      print(f"Pit result, new ai Wins: {wins}, Fails: {fails}, Draws: {draws}")

      if wins/(wins+fails) > 0.6:
        print("Accept!!! Saving checkpoint...")
        self.net.save(checkpoint_file)
        self.train_data_history = train_data
        with open(data_file, 'wb+') as f:
          pickle.dump(self.train_data_history, f)
      else:
        print("Discarding checkpoint...")
        self.net.load(tmp_checkpoint_file)

  def _run_iteration(self):
    self.ai.reset()
    iteration_data = []

    black_wins = 0
    white_wins = 0
    draws = 0
    for epoch in tqdm(range(self.iteration_epochs), desc="Self Play"):
      board = self.board.copy()

      epoch_steps = 0

      self.ai.set_board(board)

      epoch_data = []
      while not board.is_game_over():
        action = self.ai.move(int(epoch_steps <= self.temp_threshold))
        x, y = board.get_simple_data(action)
        epoch_data.extend(board.enhance_data(x, y))
        board.move(action)
        epoch_steps += 1

      winner = board.get_winner()
      if winner == 1:
          black_wins += 1
      elif winner == -1:
          white_wins += 1
      else:
          draws += 1
      print('#epoch', epoch, ', step ', epoch_steps, 'winner', winner)
      board.display()
      print('history:', [[[h[0]//board.size, h[0]%board.size], h[1]] for h in board.history])
      for data in epoch_data:
        iteration_data.append([data[0], winner, data[1][1]])
    print('summary: black wins', black_wins, 'white wins', white_wins, 'draws', draws)
    self.ai.displayPerformance()

    return iteration_data

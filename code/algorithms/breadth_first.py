from code.classes import board, cars
from code import helpers
import queue
import copy

class BreadthFirst():
    def __init__(self, board):
        self.size = board.size
        self.board = copy.deepcopy(board)
        self.cars_list = self.board.cars_list
        self.archive = {}
        self.states = queue.Queue(self.board.string_repr())
        self.best_solution = None
        self.count = 0

        self.archive[self.board] = 0


    def get_next_state(self):
        return self.states.get()

    def build_children(self):
        # find all possible boards,
        # put into archive
        # queue 
        board_strings = self.board.find_possible_boards()
    
        for board_string in board_strings:
            
            new_board = Board(self.size, car_list)
            new_board_string = new_board.string_repr()
            del(new_board)
            # if board in archive: pass
            if new_board_string in self.archive:
                continue
            # if board not in archive: add to archive and add to queue
            else:
                # heuristiek mogelijk toepassen, score, hoe goed?
                self.archive[new_board_string] = 0
                # heuristieken toepassen
                self.states.put(new_board_string)


    def run(self):
        while self.states:
            current_board = self.states.get()
            self.board.decode_str(current_board)

            if current_board.is_won():
                print("we won")
                break
            build_children(current_board)
            current_board = self.states.get()
            # board_instance = copy.deepcopy(current_board) 
            # breadth_instance = BreadthFirst(board_instance) 
            build_children(current_board)

            print(current_list)
            self.count += 1
            if self.count % 100 == 0:
                 print(f'children count:{self.count}')





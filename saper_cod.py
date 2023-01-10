import random


class Cell:  # игровые клетки

    def __init__(self, around_mines=0, mine=False, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine  # True/False наличие мины
        self.fl_open = fl_open  # открыта или закрыта кл

class GamePole:

    def __init__(self, N, M):
        self.n = N
        self.m = M
        self.pole = [[Cell() for _ in range(N)] for _ in range(N)]
        self.init(M)  # заполнение минами
        self.__count_okrug_mine()  # подсчет мин вокруг клеток

    def init(self, M):  # функ заполн. минами
        count_pole = self.n ** 2
        list_count_pole = range(1, count_pole + 1)  # номера всех игровых клеток
        mine_pole = random.sample(list_count_pole, M)  # номера клеток с минами
        count = 0
        for i in range(self.n):
            for j in range(self.n):
                count += 1
                if count in mine_pole:
                    x = self.pole[i][j]
                    x.mine = True

    def __count_okrug_mine(self):  # колличество мин вокруг клеток
        for i in range(self.n):
            for j in range(self.n):
                if self.pole[i][j].mine == True:
                    continue
                else:
                    spis = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i - 1, j - 1),
                            (i - 1, j + 1), (i + 1, j - 1)]
                    valid_spis = list(filter(lambda x: 0 <= x[0] < self.n and 0 <= x[1] < self.n, spis))  # фильтр чтобы не выходить за рамки
                    x = self.__count_mine_loca(valid_spis)
                    self.pole[i][j].around_mines = x

    def __count_mine_loca(self, valid_spis):  #  вспомогательная функ. подсчет мин
        res = 0
        for i in valid_spis:
            x, y = i[0], i[1]
            if self.pole[x][y].mine == True:
                res += 1
        return res


    def show(self):  # отображение игрового поля
        for raw in self.pole:
            for i in raw:
                if i.mine == True:
                    print('*', end = ' ')
                    continue
                if i.around_mines > 0:
                    print(i.around_mines, end = ' ')
                    continue
                if i.fl_open == False:
                    print('#', end = ' ')
            print()

pole_game = GamePole(10, 12)
pole_game.show()
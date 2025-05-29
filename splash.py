from PyQt6 import QtGui,QtWidgets


#Splash Ekranı
class MovieSplashScreen(QtWidgets.QSplashScreen):

	def __init__(self, pathToGIF):
		self.movie = QtGui.QMovie(pathToGIF)
		self.movie.jumpToFrame(0)
		pixmap = QtGui.QPixmap(self.movie.frameRect().size())
		QtWidgets.QSplashScreen.__init__(self, pixmap)
		self.movie.frameChanged.connect(self.repaint)

	def showEvent(self, event):
		self.movie.start()

	def hideEvent(self, event):
		self.movie.stop()

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		pixmap = self.movie.currentPixmap()
		self.setMask(pixmap.mask())
		painter.drawPixmap(0, 0, pixmap)
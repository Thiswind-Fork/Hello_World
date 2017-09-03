from PythonCard import model

class MainWindow(model.Background):
    pass

app = model.Application(MainWindow)
app.MainLoop()

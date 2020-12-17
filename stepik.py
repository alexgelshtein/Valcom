def my_decorator(func):
  def wrapper():
    print('Before func')
    func()
    print('After func')
  return wrapper()

@my_decorator
def sec():
  print('Func line')
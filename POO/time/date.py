class Fecha:
  def __init__(self, day: int, month: int, year: int):
    self.setYear(year)
    self.setMonth(month)
    self.setDay(day)
  
  
  def setYear(self, year: int) -> None:
    if year > 0:
      self._year = year
    else:
      raise ValueError("Year must be positive")

  def getYear(self) -> int:
    return self._year

  def setMonth(self, month: int) -> None:
    if 1 <= month <= 12:
      self._month = month
  def getMonth(self) -> int:
    return self._month
  
  def setDay(self, day) -> None:
    if

  def getDay(self) -> int:


  def _days_in_month(self):


  def _is_leap_year(self):

"""
some method to increment day/month/year
      and:
__eq__
__gt__
__lt__
"""

  def __str__(self):
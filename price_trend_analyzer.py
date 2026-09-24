def get_closing_prices ()->tuple [list[float] , str]:
  stock_name = input("Enter the stock name: ")
  closing_prices = []
  days_to_analyze = int(input("How many days do you want to analyze? "))
  for day in range(days_to_analyze):
    closing_price = float(input(f"Enter the closing price for day {day+1}: "))
    closing_prices.append(closing_price)
  return closing_prices , stock_name
  
def Basic_Statistics(closing_prices:list[float] , stock_name:str)-> tuple[float,float,float,float]:
  highest_price = max(closing_prices)
  lowest_price = min(closing_prices)
  average_price = sum(closing_prices) / len(closing_prices)
  volatility = highest_price - lowest_price
  statistic_values =[highest_price,lowest_price,average_price,volatility]
  return highest_price,lowest_price,average_price,volatility
  
def get_bullish_trend_analysis(closing_prices: list[float]) -> list[int]:
    max_streak = []
    current_streak = [1]
    for i in range(1, len(closing_prices)):
        if closing_prices[i] >= closing_prices[i-1]:
            current_streak.append(i + 1)
        else:
            if len(current_streak) > len(max_streak):
                max_streak = current_streak
            current_streak = [i + 1]
    if len(current_streak) > len(max_streak):
        max_streak = current_streak
    return max_streak
  
def calculate_overall_performance(closing_prices: list[float]) -> float:
    if not closing_prices or closing_prices[0] == 0:
        return 0.0
    price_change = closing_prices[-1] - closing_prices[0]
    percentage_change = price_change / closing_prices[0] * 100
    return percentage_change

def analyze_single_stock():
  closing_prices , stock_name = get_closing_prices()
  
  statistics = Basic_Statistics(closing_prices , stock_name)
  Statistical_Operations = ["highest_price" ,"lowest_price", "average_price", "volatility"]
  for i in range(len(Statistical_Operations)):
    print(f"{Statistical_Operations[i]} is: {statistics[i]}")
    
  max_streak = get_bullish_trend_analysis(closing_prices)
  print(f"Longest rising streak: {max_streak} ({len(max_streak)} days)")

  overall_performance = calculate_overall_performance(closing_prices)
  if overall_performance > 0 :
    print(f"The stock had a positive overall performance of {overall_performance}%.")
  elif overall_performance <  0:
    print(f"The stock had a negative overall performance of {abs(overall_performance)}%.")
  else:
    print("The stock had no overall change in performance.")

def get_stocks_data ():
  stock1_closing_prices , stock1_name = get_closing_prices ()
  stock1_statistics = Basic_Statistics(stock1_closing_prices,stock1_name)
  stock1_average = stock1_statistics[2]
  stock1_volatility = stock1_statistics[3]
  stock1_max_streak = get_bullish_trend_analysis (stock1_closing_prices)
  stock1_overall_performance = calculate_overall_performance(stock1_closing_prices)
  print("-"*10)
  stock2_closing_prices , stock2_name = get_closing_prices ()
  stock2_statistics= Basic_Statistics(stock2_closing_prices,stock2_name)
  stock2_average = stock2_statistics[2]
  stock2_volatility = stock2_statistics[3]
  stock2_max_streak = get_bullish_trend_analysis (stock2_closing_prices)
  stock2_overall_performance = calculate_overall_performance(stock2_closing_prices)

  return stock1_name ,stock1_average ,stock1_volatility ,stock1_max_streak ,stock1_overall_performance, stock2_name ,stock2_average ,stock2_volatility ,stock2_max_streak,stock2_overall_performance

  
def compare_stocks(stock1_name ,stock1_average ,stock1_volatility ,stock1_max_streak ,stock1_overall_performance, stock2_name ,stock2_average ,stock2_volatility ,stock2_max_streak,stock2_overall_performance):
  
  print(f"Comparison Results: {stock1_name} vs {stock2_name}")
  if stock1_overall_performance > stock2_overall_performance:
    print(f"{stock1_name} has a higher overall performance: {stock1_overall_performance}% vs {stock2_overall_performance}%")
  elif stock2_overall_performance > stock1_overall_performance:
    print(f"{stock2_name} has a higher overall performance: {stock2_overall_performance}% vs {stock1_overall_performance}%")
  else:
    print("Both stocks have the same overall performance.")
    
  if stock1_volatility < stock2_volatility:
        print(f"{stock1_name} has lower volatility (more stable): {stock1_volatility} vs {stock2_volatility}")
  elif stock2_volatility < stock1_volatility:
        print(f"{stock2_name} has lower volatility (more stable): {stock2_volatility} vs {stock1_volatility}")
  else:
       print("Both stocks have the same volatility.")

  if len(stock1_max_streak) > len(stock2_max_streak):
    print(f"{stock1_name} has a longer maximum rising streak: {len(stock1_max_streak)} days vs {len(stock2_max_streak)} days.")
  elif len(stock2_max_streak) > len(stock1_max_streak):
    print(f"{stock2_name} has a longer maximum rising streak: {len(stock2_max_streak)} days vs {len(stock1_max_streak)} days.")
  else:
    print(f"Both stocks have the same maximum rising streak: {len(stock2_max_streak)} days.")

  if stock1_average > stock2_average:
    print(f"{stock1_name} has a higher average price: {stock1_average} vs {stock2_average}.")
  elif stock2_average > stock1_average:
    print(f"{stock2_name} has a higher average price: {stock2_average} vs {stock1_average}.")
  else:
    print(f"Both stocks have the same average price: {stock1_average}.")

def main():
  options = ["1. Analyze a Single Stock","2. Compare Two Stocks","3. Exit"]
  while True:
    for op in options:
      print(op)
    try :
      choice = int(input("Enter your choice: "))
    except ValueError:
        print("invalid input")
        continue
    if choice == 1:
      analyze_single_stock( )
      continue
    elif choice == 2:
      all_stocks_data = get_stocks_data()
      compare_stocks(*all_stocks_data)
      continue
    elif choice == 3:
      break
    else:
      print("Invalid choice. Please select 1, 2, or 3.")
if __name__ == "__main__":
  main()

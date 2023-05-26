
#include "fibonacci.hpp"

#include <gtest/gtest.h>

TEST(Fibonacci, CalcSmall) {
  EXPECT_EQ(55, calcFibonacci(10));
  EXPECT_EQ(6765, calcFibonacci(20));
}

TEST(Fibonacci, CalcBig) {
  //
  EXPECT_EQ(1134903170, calcFibonacci(45));
}

TEST(Fibonacci, Series) {
  const std::vector<int> expected = {0, 5, 55};

  SeriesCalculator calc;

  calc.putIndex(0);
  calc.putIndex(5);
  calc.putIndex(10);

  EXPECT_EQ(expected, calc.calc());
}
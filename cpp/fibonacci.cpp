
#include "fibonacci.hpp"

int calcFibonacci(const int index) {
  if (index <= 1) {
    return index;
  }

  return calcFibonacci(index - 1) + calcFibonacci(index - 2);
}

std::vector<int> SeriesCalculator::calc() const {
  std::vector<int> result;
  result.reserve(m_indexes.size());

  for (const auto &index : m_indexes) {
    result.push_back(calcFibonacci(index));
  }

  return result;
}

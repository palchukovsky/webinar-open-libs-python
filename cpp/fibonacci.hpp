#pragma once

#include <vector>

[[nodiscard]] int calcFibonacci(int index);

class SeriesCalculator {
 public:
  void putIndex(const int index) { m_indexes.push_back(index); }

  [[nodiscard]] std::vector<int> calc() const;

 private:
  std::vector<int> m_indexes;
};
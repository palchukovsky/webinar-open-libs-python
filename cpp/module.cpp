
#include "fibonacci.hpp"

#include <pybind11/pybind11.h>
#include <pybind11/stl_bind.h>

PYBIND11_MAKE_OPAQUE(std::vector<int>);

PYBIND11_MODULE(pyfibonacci, module) {
  //

  // Optional module docstring.
  module.doc() =
      "PyFibonacci module. Open webinar live part"
      " - how to build C++ libraries, how to use them in C++, and not only.";
  //

  // Adding function to the module:
  module.def("calc", &calcFibonacci, "Fibonacci number calculation.",
             pybind11::arg("index"));
  //

  // Adding class to the module:
  pybind11::class_<SeriesCalculator>(module, "SeriesCalculator")
      .def(pybind11::init<>())
      .def("put_index", &SeriesCalculator::putIndex, pybind11::arg("index"))
      .def("calc", &SeriesCalculator::calc);
  //

  // Binding used containers:
  pybind11::bind_vector<std::vector<int>>(module, "IntList");

  // Adding variables:
  module.attr("the_answer") = 42;
  {
    pybind11::object world = pybind11::cast("World");
    module.attr("what") = world;
  }

  //
}
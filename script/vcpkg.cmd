cd ..

git clone https://github.com/Microsoft/vcpkg.git

.\vcpkg\bootstrap-vcpkg.bat
.\vcpkg\vcpkg integrate install

.\vcpkg\vcpkg list

.\vcpkg\vcpkg install pybind11
.\vcpkg\vcpkg install gtest

.\vcpkg\vcpkg list
from conans import ConanFile, CMake, tools
from conan.tools.cmake import CMakeToolchain

class RosIndustrialCmakeBoilerplateConan(ConanFile):
    name = "ros_industrial_cmake_boilerplate"
    version = "0.3.0"

    license = "Apache 2.0"
    author = "Levi Armstrong"
    url = ""
    description = ""
    topics = ("")
    
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True}
    
    # generators = "cmake_find_package"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        git = tools.Git(folder='ros_industrial_cmake_boilerplate')
        git.clone('https://github.com/ros-industrial/ros_industrial_cmake_boilerplate.git')
        git.checkout('0.3.0')

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder='ros_industrial_cmake_boilerplate/ros_industrial_cmake_boilerplate')
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()


    def package_info(self):
        self.cpp_info.libs = ["ros_industrial_cmake_boilerplate"]

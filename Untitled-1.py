# # # Import required modules
# # from abc import ABC, abstractmethod


# # class Car(ABC):
# #     def __init__(self, brand, model, year):
# #         self.brand = brand
# #         self.model = model
# #         self.year = year

# #     # Create abstract method
# #     @abstractmethod
# #     def printDetails(self):
# #         pass

# #     # Create concrete method
# #     def accelerate(self):
# #         print("speed up ...")

# #     def break_applied(self):
# #         print("Car stop")


# # # Create a child class
# # class Hatchback(Car):
# #     def printDetails(self):
# #         print("Brand:", self.brand)
# #         print("Model:", self.model)
# #         print("Year:", self.year)

# #     def Sunroof(self):
# #         print("Not having this feature")

# #     # Create a child class


# # class Suv(Car):
# #     def printDetails(self):
# #         print("Brand:", self.brand)
# #         print("Model:", self.model)
# #         print("Year:", self.year)

# #     def Sunroof(self):
# #         print("Available")


# # car1 = Hatchback("Maruti", "Alto", "2022")
# # car1.printDetails()
# # car1.accelerate()
# # car1.Sunroof()
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius

#     @property
#     def radius(self):
#         return self.__radius

#     # @radius.getter
#     # def radius(self):
#     #     return self._radius

#     @radius.setter
#     def radius(self, value):
#         if value <= 0:
#             raise ValueError("Radius must be a positive value.")
#         self.__radius = value

#     @property
#     def area(self):
#         return 3.14 * self.__radius * self.__radius


# # Creating an instance of the Circle class
# my_circle = Circle(5)

# print(my_circle.__radius)

# # Accessing the radius property
# print(my_circle.radius)  # Output: 5

# # Setting a new radius using the property setter
# my_circle.radius = 7

# # Accessing the updated radius and area
# print(my_circle.radius)  # Output: 7
# print(my_circle.area)  # Output: 153.86

## Car Reservation

Vehicle & Car Reservation System Manages Vehicle Reservations and tracks locations on Google map.



#### Available in version
- Version 15
___
#### How to Install App in ERPNext Version-15
1. `bench get-app https://github.com/Solufy-ERPNext-Apps/car_reservation.git --branch 15.0`
2. `bench --site [your.site.name] install-app car_reservation`
3. `bench migrate`
4. `bench clear-cache`

## Features of  Car Reservation 

*  Car can be booked in advance for the trip
* Trip start location and end location distance recorder with kilometer
* Car new trip start with odometer kilometer noted
* Car registrations details are tracked
* Car services record are maintained 
* Car driver details records  with name and license number.
* Availability of the car can be Tracked
* Registration Process of cars tracked with different stages.
* Vehicle specification details like, company make, model, License plate, chassis number, Seats Number, Doors number, Color, Model year Fuel type, Horsepower, records are maintained
* Car Contract details are recorded with the history
* Car removed from the operations automatically as the contract of the car expired.
* Odometer details are updated automatically based on ride done by driver or update odometers record
* Customers can not book the car trip while the car is in the reserved stage.
* Once the Car trip is done, the car is automatically available for the new trip.
* Approver can only approve the reservation of the car.



#### ➤ Key Reports of the car reservation: 

* Car Reservation Details
* Contract Details
* Vehicle Information
* Driver Details
* Car Service Details


#### License

MIT

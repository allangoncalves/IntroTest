package imd0412.parkinglot.calculator;

import imd0412.parkinglot.ParkingLotType;

public class Calculator {

	private int minute;
	private int hour;
	private int dayOfMonth;
	private int month;
	private int year;





	/**
	 * Calculates the staying cost in the parking lot.
	 * 
	 * @param checkin String representing check-in date. String follows the format "yyyy.MM.dd HH:mm".
	 * @param checkout String representing check-out date. String follows the format "yyyy.MM.dd HH:mm".
	 * @param type
	 * @return
	 */
	Float calculateParkingCost(String checkin, String checkout, ParkingLotType type) {
		try{
			DateTimeFormatter DATE_FORMATTER = DateTimeFormatter.ofPattern("yyyy.MM.dd HH:mm";);
			LocalDateTime checkinTime = LocalDateTime.parse(checkin, DATE_FORMATTER);
			LocalDateTime checkoutTime = LocalDateTime.parse(checkout, DATE_FORMATTER);
			Duration duration = Duration.between(checkinTime, checkoutTime);
			long days = duration.toDays();
			long hours = duration.toHours();
			long minutes = duration.toMinutes();
		}
		catch(DateTimeParseException e){
			System.err.printf("not parsable!%n");
			throw e;
		}
		


		if(ParkingLotType.ShortTerm.equals(type)){
			if(hours<1 && days==0){
				return 8.00;
			}
			else if(hours>1 && hours<=24 && days==0){
				if(minutes>=1)
					return 8.00 + (hours)*2;
				else{
					return 8.00 + (hours-1)*2;
				}
			}
			else if(hours>24 && days<=7){
				if(minutes>=1)
					return 8.00 + (hours-1)*2 + days*50.00;
				else{
					return 8.00 + (hours)*2 + days*50.00;
				}
			}
			else if(days>7){
				return 8.00 + (hours)*2 + 350.00 + (days-7)*30.00;
			}
		}
		else if(ParkingLotType.LongTerm.equals(type)){
			if(hours<=24 && days<=1){
				if(minutes>=1)
					return 70.00 + 50.00;
				else{
					return 70.00;
				}
			}
			else if(days>=1 && days<=7){
				if(minutes>=1 || hours>=1){
					return 70.00 + days*50.00;
				}
				else if(minutes==0 && hours==0){
					return 70.00 + (days-1)*50.00;
				}
			}
			else if(days>7 && days<30){
				if(minutes>=1 || hours>=1){
					return 70.00 + 350.00 + (days-6)*30.00;
				}
				else if(minutes==0 && hours==0){
					return 70.00 + 350.00 + (days-7)*30.00;
				}	
			}
			else if(days>=30){
				if(minutes>=1 || hours>=1){
					return 70.00 + 350.00 + (days-6)*30.00 + 500.00;
				}
				else if(minutes==0 && hours==0){
					return 70.00 + 350.00 + (days-7)*30.00 + 500.00;
				}	
			}
		}
		else if(ParkingLotType.VIP.equals(type)){
			if(days<7){
				return 500.00;
			}
			else if(days==7){
				if(minutes==0 && hours==0){
					return 500.00;
				}
				else{
					return 500.00 + 100.00;
				}
			}
			else if(days>7 && days<=14){
				if(minutes==0 && hours==0){
					return 500.00 + (days-7)*100.00;
				}
				else{
					return 500.00 + (days-6)100.00;
				}	
			}
			else if(days>14){
				if(minutes==0 && hours==0){
					return 500.00 + 700.00 + (days-14)*80.00;
				}
				else{
					return 500.00 + 700.00 + (days-13)*80.00;
				}
			}
		}
	}

	public getInfo(){
		int minute = checkinTime.getMinute();
		int hour = checkinTime.getHour();
		int dayOfMonth = checkinTime.getDayOfMonth();
		int month = checkinTime.getMonth().getValue();
		int year = checkinTime.getYear();
	}
}

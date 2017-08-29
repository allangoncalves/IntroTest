package imd0412.parkinglot.calculator;

import org.junit.Assert;
import org.junit.Test;


@RunWith(value = Parametherized.class)
public class CalculatorTest
{

	@parameters
	public static Collection<Object[]> data(){
		return Arrays.asList(new Object[][]{
			{"yyyy.MM.dd HH:mm","yyyy.MM.dd HH:mm", parkingLotType.ShortTerm},
			{},
			{},
			{},
			{},
			{}
		});
	}
	private String checkin;
	private String checkout
	ParkingLotType type;
	private Float expected;

	public CalculatorTest(String checkin, String checkout, ParkingLotType type, Float expected){
		this.checkin = checkin;
		this.checkout = checkout;
		this.type = type;
		this.expected = expected;	
	}

	@Test
	public void realCostTest(){
		Calculator c = Calculator()
		assertEquals(c.calculateParkingCost(this.checkin, this.checkout, this.type), this.expected);
	}
}

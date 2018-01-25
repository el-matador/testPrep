import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;

public class MinSlot {

	public void findMinSlot(List<Integer> jobList , int coolPeriod) {
		
		int len = jobList.size();
		int i=0;
		int j=1;
		
		HashMap<Integer, Integer> coolMap = new HashMap<Integer, Integer>();
		for(int l =0; l<jobList.size() ; l++) {
			coolMap.put(jobList.get(l), 0);
		}
		
		List<String> output = new ArrayList<String>();
		output.add(String.valueOf(jobList.get(i)));
		coolMap.put(jobList.get(i), coolPeriod);
		
		while(j<len) {
			int dec = 0;
			if(jobList.get(j) == jobList.get(i)) {
				for (int k = 0; k < coolPeriod; k++) {
					output.add("-");
					dec++;
				}
				
				output.add(String.valueOf(jobList.get(j)));
				dec++;
			}
			else {
				int cool = coolMap.get(jobList.get(j));
				for (int k = 0; k < cool; k++) {
					output.add("-");
					dec++;
				}
				
				output.add(String.valueOf(jobList.get(j)));
				dec++;
			}
			for(Entry<Integer, Integer> entry : coolMap.entrySet()) {
				if(entry.getKey() == jobList.get(j) ) {
					//reset cooling period
					coolMap.put(entry.getKey(), coolPeriod);
				};[
				else {
					//decrement cool period
					int cool = entry.getValue() ==0 ? 0 : entry.getValue() - dec;
					coolMap.put(entry.getKey(), cool);
				}
			}
			i++;
			j++;
		}
		
		System.out.println("Interval : " + output.size());
		
		System.out.println("Output list : ");
		
		for(int l =0; l<output.size() ; l++) {
			System.out.print(" " + output.get(l));
		}
	}
	
	public static void main(String[] args) {
		
		MinSlot obj = new MinSlot();
		
		/*
		 	Tasks: 1, 1, 2, 1
			Recovery interval (cooldown): 2
			Output: 7  (order is 1 _ _ 1 2 _ 1)

		 */
		int coolPeriod = 2;
		List<Integer> jobList = new ArrayList<Integer>();
		jobList.add(1);
		jobList.add(1);
		jobList.add(2);
		jobList.add(1);
		
		obj.findMinSlot(jobList, coolPeriod);
		
		System.out.println("\n\n\n");
		
		/*
		 
	 		Tasks: 1, 1, 2, 1
			Recovery interval (cooldown): 2
			Output: 7  (order is 1 _ _ 1 2 _ 1)					

		 */
		 coolPeriod = 3;
		 
		 jobList.clear();
		
		 jobList.add(1);
		 jobList.add(2);
		 jobList.add(3);
		 jobList.add(1);
		 jobList.add(2);
		 jobList.add(3);
		 
		 obj.findMinSlot(jobList, coolPeriod);
	}
}

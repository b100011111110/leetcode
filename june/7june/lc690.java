class Solution {
    Map<Integer,Employee> gemployees = new HashMap<>();
    int traverse(Employee root){
        int c = 0;
        for(int e:root.subordinates){
            c += traverse(gemployees.get(e));
        }
        return root.importance + c;
    }
    public int getImportance(List<Employee> employees, int id) {
        for(Employee e:employees){
            gemployees.put(e.id,e);
        }
        return traverse(gemployees.get(id));
    }
}
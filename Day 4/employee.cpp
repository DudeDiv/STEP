class Employee
{
    private String empId;
    private String name;
    private Address address;

    public void setEmpId(String empId)
    {
        this.empId = empId;
    }
    public String getEmpId()
    {
        return this.empId;
    }
    public void setName(String name)
    {
        this.name = name;
    }
    public String getName()
    {
        return this.name;
    }
    public void setAddress(Address address)
    {
        this.address = address;
    }
    public Address getAddress()
    {
        return this.address;
    }
   
}

class Address {
    private String line1;
    private String line2;
    private String city;
    private String pinCode;

    // Getter and Setter for line1
    public String getLine1() {
        return line1;
    }

    public void setLine1(String line1) {
        this.line1 = line1;
    }

    // Getter and Setter for line2
    public String getLine2() {
        return line2;
    }

    public void setLine2(String line2) {
        this.line2 = line2;
    }

    // Getter and Setter for city
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    // Getter and Setter for pinCode
    public String getPinCode() {
        return pinCode;
    }

    public void setPinCode(String pinCode) {
        this.pinCode = pinCode;
    }
}

class DisplayForm
{
    public void displayEmployee(Employee emp)
    {
        System.out.println("Emp ID : " + emp.getEmpId());
        System.out.println("Name : " + emp.getName());
        System.out.println("Line 1 : " + emp.getAddress().getLine1());
        System.out.println("Line 2 : " + emp.getAddress().getLine2());
        System.out.println("City : " + emp.getAddress().getCity());
        System.out.println("PinCode : " + emp.getAddress().getPinCode());
    }
}

class Main {
    public static void main(String[] args) {
        Employee emp = new Employee();
        emp.setEmpId("1001");
        emp.setName("Mayank");
       
        Address a1 = new Address();
       
        a1.setLine1("11, SRM TP ");
        a1.setLine2("New Campus  Road ");
        a1.setCity("Chennai");
        a1.setPinCode("600015");
       
        emp.setAddress(a1);     // coonect the objects
       
        DisplayForm form = new DisplayForm();
        form.displayEmployee(emp);
       
    }
}

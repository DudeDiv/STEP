import java.util.*;

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

class Company
{
    private String name;
    private String dtInc;
   
    private List<Employee> employees;
   
    public void setEmployees(List<Employee> employees)
    {
        this.employees = employees;
    }
    public void addEmployee(Employee e)
    {
        employees.add(e);
    }
    List<Employee> getEmployees()
    {
        return employees;   // return the array    
    }
   
    void setName(String name)
    {
        this.name = name;
    }
   
    String getName()
    {
        return name;
    }
   
    void setDtInc(String dtInc)
    {
        this.dtInc = dtInc;
    }
   
    String getDtInc()
    {
        return dtInc;
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
    public void displayAddress(Address address)
    {
        System.out.println("Line 1 : " + address.getLine1());
        System.out.println("Line 2 : " + address.getLine2());
        System.out.println("City : " + address.getCity());
        System.out.println("PinCode : " + address.getPinCode());
    }
   
    public void displayCompany(Company c)
    {
        System.out.println("--------------------------------------------");
        System.out.println("Company Name : " + c.getName());
        System.out.println("Company Dt Incorp.  : " + c.getDtInc());
       
        System.out.println("--------------------------------------------");
        List<Employee> employees = c.getEmployees();
       
        for(Employee e : employees)
        {
            displayEmployee(e);
            System.out.println();
        }
       
        System.out.println("--------------------------------------------");
    }
}

class ObjectBuilder
{
    public static Address makeAddress(String line1, String line2, String city, String pinCode)
    {
        Address a = new Address();
        a.setLine1(line1);
        a.setLine2(line2);
        a.setCity(city);
        a.setPinCode(pinCode);
       
        return a;
    }
   
    public static Employee makeEmployee(String empId, String name, Address address)
    {
        Employee e = new Employee();
        e.setEmpId(empId);
        e.setName(name);
        e.setAddress(address);
       
        return e;
    }
   
    public static Company makeCompany(String name, String dtInc, List<Employee> employees)
    {
        Company c = new Company();
        c.setName(name);
        c.setDtInc(dtInc);
       
        List<Employee> mEmployees = new ArrayList<Employee>();
       
        c.setEmployees(mEmployees);
       
        for(Employee e : employees)
        {
            c.addEmployee(e);
        }
       
        return c;
    }
}
class Main {
    public static void main(String[] args) {
        Address a1 = ObjectBuilder.makeAddress("11, SRM TP ","New Campus  Road ","Chennai","600015");
       
        Address a2 = ObjectBuilder.makeAddress("18, SRM VS ","Old Campus  Road ","Chennai","600015");
       
        Employee e1 = ObjectBuilder.makeEmployee("1001","Mayank",a1);
       
        Employee e2 = ObjectBuilder.makeEmployee("1002","Madhav",a2);
       
        List<Employee> eArr = new ArrayList<Employee>();
        eArr.add(e1);
        eArr.add(e2);

        Company c1 = ObjectBuilder.makeCompany("TGL","20-Jun-2024",eArr);      
       
        DisplayForm form = new DisplayForm();
        form.displayCompany(c1);
    }
}

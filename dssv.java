import java.util.LinkedList;
import java.util.Scanner;

class Student{
    String id;
    String name;

    public Student(String id, String name){
        this.id = id;
        this.name= name;

    }
    @Override
    public String toString(){
        return "ID: "+ id+ " | NAME: " + name;

    }
}
public class AttendanceList{
    public static void main(String[] arg){
        LinkedList <Student>list =new LinkedList<>();
        Scanner scanner = new Scanner(System.in);
        int choice;

        do{
            System.out.println("\n==== QUẢN LÝ ĐIỂM DANH ===");
            System.out.println("1. Thêm sinh viên điểm danh");
            System.out.println("2. Xóa sinh viên khỏi danh sách");
            System.out.println("3. Hiển thị danh sách điểm danh");
            System.out.println("4. Thoái");
            System.out.print("Lựa chọn...");
            choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice){
                case 1:
                System.out.print("Nhập ID: ");
                String id= scanner.nextLine();
                System.out.print("Nhập tên: ");
                String name = scanner.nextLine();
                list.add(new Student(id,name));
                System.out.println("Đã thêm sinh viên.");
                break;

                case 2:
                if(!list.isEmpty()){
                    System.out.println("Nhập ID sinh viên cần xóa...");
                    String delId = scanner.nextLine();
                    list.removeIf(student ->student.id.equals(delId));
                    System.out.println("Đã xóa sinh viên có ID: "+ delId);

                }
                else{
                    System.out.println("Danh sách rỗng.");

                }
                break;

                case 3:
                    System.out.println("\nDanh sách điểm danh: ");
                    if(list.isEmpty()){
                        System.out.println("Chưa có sinh viênc nào điểm danh.");

                    }
                    else {
                        for(Student s : list){
                            System.out.println(s);
                        }

                    }
                    break;
                case 4:
                System.out.println("Thoat chương trình...");
                break;
                    default:
                    System.out.println("Lựa chọn không hợp lệ... thử lại...");
            }
            
            

        }while (choice!=4);
        scanner.close();
    }
}

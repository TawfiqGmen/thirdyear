import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.sql.*;

public class DepartmentHead {
    private static final String JDBC_URL = "jdbc:mysql://localhost:3306/studentmarksmanagement";
    private static final String USERNAME = "root";
    private static final String PASSWORD = "";


 public void grantmarksPrivilages(){
     String url = "jdbc:mysql://localhost:3306/studentmarksmanagement";
     String user = "root";
     String password = "";

     try (Connection conn = DriverManager.getConnection(url, user, password)) {
         Statement stmt = conn.createStatement();
         String grantQuery = "GRANT SELECT, INSERT, UPDATE, DELETE ON marks_table TO 'departmenthead'@'localhost'";
         stmt.executeUpdate(grantQuery);
         System.out.println("Privileges granted successfully.");
     } catch (SQLException e) {
         e.printStackTrace();
     }

 }

    public void grantsudentPrivilages(){
        String url = "jdbc:mysql://localhost:3306/studentmarksmanagement";
        String user = "root";
        String password = "";

        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            Statement stmt = conn.createStatement();
            String grantQuery = "GRANT SELECT, INSERT, UPDATE, DELETE ON student TO 'departmenthead'@'localhost'";
            stmt.executeUpdate(grantQuery);
            System.out.println("Privileges granted successfully.");
        } catch (SQLException e) {
            e.printStackTrace();
        }

    }


    public void createMarks(int student_Id, String subject, int marks) {
        grantmarksPrivilages();
        grantsudentPrivilages();
        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/studentmarksmanagement", "root", "");
             PreparedStatement preparedStatement = connection.prepareStatement("INSERT INTO marks_table (student_id, subject, marks) VALUES (?, ?, ?)")) {
            preparedStatement.setInt(1, student_Id);
            preparedStatement.setString(2, subject);
            preparedStatement.setInt(3, marks);
            preparedStatement.executeUpdate();
            System.out.println("Marks added successfully.");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void createstudent(int Id, String name) {
        grantmarksPrivilages();
        grantsudentPrivilages();
        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/studentmarksmanagement", "root", "");
             PreparedStatement preparedStatement = connection.prepareStatement("INSERT INTO student (id,name) VALUES (?, ?)")) {
            preparedStatement.setInt(1,Id);
            preparedStatement.setString(2, name);
            preparedStatement.executeUpdate();
            System.out.println("students added successfully.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void readMarks(int studentId) {
        grantmarksPrivilages();
        grantsudentPrivilages();
        displayTableFromDatabase();
    }

    public void updateMarks(int studentId, String subject, int newMarks) {
        grantmarksPrivilages();
        grantsudentPrivilages();
        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/studentmarksmanagement", "root", "");
             PreparedStatement preparedStatement = connection.prepareStatement(
                     "UPDATE marks_table SET marks = ? WHERE student_id = ? AND subject = ?")) {

            preparedStatement.setInt(1, newMarks);
            preparedStatement.setInt(2, studentId);
            preparedStatement.setString(3, subject);
            preparedStatement.executeUpdate();

            System.out.println("Marks updated successfully.");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void deleteMarks(int studentId, String subject) {
        grantmarksPrivilages();
        grantsudentPrivilages();
        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/studentmarksmanagement", "root", "");
             PreparedStatement preparedStatement = connection.prepareStatement(
                     "DELETE FROM marks_table WHERE student_id = ? AND subject = ?")) {

            preparedStatement.setInt(1, studentId);
            preparedStatement.setString(2, subject);
            preparedStatement.executeUpdate();

            System.out.println("Marks deleted successfully.");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }





    private static void displayTableFromDatabase() {
        try (Connection connection = DriverManager.getConnection(JDBC_URL, USERNAME, PASSWORD);
             Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery("SELECT * FROM marks_table ")) {

            DefaultTableModel model = new DefaultTableModel();

            model.addColumn("Student ID");
            model.addColumn("Subject");
            model.addColumn("Marks");

            while (resultSet.next()) {
                Object[] rowData = {resultSet.getInt("student_id"), resultSet.getString("subject"), resultSet.getInt("marks")};
                model.addRow(rowData);
            }
            JTable table = new JTable(model);
            table.setAutoResizeMode(JTable.AUTO_RESIZE_ALL_COLUMNS);
            JScrollPane scrollPane = new JScrollPane(table);
            JFrame frame = new JFrame("Student Marks");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(600, 400);
            frame.getContentPane().add(scrollPane, BorderLayout.CENTER);
            frame.setVisible(true);

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}




import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.sql.*;

public class Student {
    private static final String JDBC_URL = "jdbc:mysql://localhost:3306/studentmarksmanagement";
    private static final String USERNAME = "root";
    private static final String PASSWORD = "";

    public String name;
    public int id;

    public Student(String name, int id) {
        this.name = name;
        this.id = id;
    }

    public boolean authenticate() {
        try (Connection connection = DriverManager.getConnection(JDBC_URL, USERNAME, PASSWORD);
             PreparedStatement preparedStatement = connection.prepareStatement(
                     "SELECT COUNT(*) AS count FROM Student WHERE name = ? AND id = ? ")) {
            preparedStatement.setString(1, name);
            preparedStatement.setInt(2, id);

            try (ResultSet resultSet = preparedStatement.executeQuery()) {
                if (resultSet.next() && resultSet.getInt("count") > 0) {
                    return true;
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return false;
    }
    public void readMarks() {
        displayTableFromDatabase();
    }

    private static void displayTableFromDatabase() {
        try (Connection connection = DriverManager.getConnection(JDBC_URL, USERNAME, PASSWORD);
             Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery("SELECT * FROM marks_table")) {

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

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Student Marks Management form");
        frame.setSize(400, 300);
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);


        JLabel userTypeLabel = new JLabel("Select User Type:");
        userTypeLabel.setBounds(50, 50, 120, 25);
        frame.add(userTypeLabel);

        String[] userTypes = {"Student", "Department Head"};
        JComboBox<String> userTypeComboBox = new JComboBox<>(userTypes);
        userTypeComboBox.setBounds(180, 50, 120, 25);
        frame.add(userTypeComboBox);

        JButton loginButton = new JButton("Login");
        loginButton.setBounds(150, 100, 100, 30);
        frame.add(loginButton);


        loginButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String selectedUserType = (String) userTypeComboBox.getSelectedItem();
                if (selectedUserType.equals("Student")) {

                    String studentName = JOptionPane.showInputDialog(frame, "Enter  Name:");
                    int studentID = Integer.parseInt(JOptionPane.showInputDialog(frame, "Enter  ID:"));

                    Student student = new Student(studentName,studentID);
                    if (student.authenticate()) {
                        student.readMarks();
                    } else {
                        JOptionPane.showMessageDialog(frame, "its not you ");
                    }
                }
                else if (selectedUserType.equals("Department Head")) {

                    String action = JOptionPane.showInputDialog(frame, "chose oneOf(create, read, update, delete):");
                    DepartmentHead departmentHead = new DepartmentHead();

                    switch (action.toLowerCase()) {
                        case "create":
                            int Id = Integer.parseInt(JOptionPane.showInputDialog(frame, "enter order number: "));
                            String name = JOptionPane.showInputDialog(frame, "Enter student name : ");
                            int studentID = Integer.parseInt(JOptionPane.showInputDialog(frame, "Enter Student ID:"));
                            String subject = JOptionPane.showInputDialog(frame, "Enter Subject:");
                            int marks = Integer.parseInt(JOptionPane.showInputDialog(frame, "Enter Marks:"));
                            departmentHead.createstudent(Id, name);
                            departmentHead.createMarks(studentID, subject, marks);
                            break;
                        case "read":
                            int readStudentID = Integer.parseInt(JOptionPane.showInputDialog(frame, "Enter Student ID:"));
                            departmentHead.readMarks(readStudentID);
                            break;
                        case "update":
                            createAndShowGUI();
                            break;
                        case "delete":
                            int deleteStudentID = Integer.parseInt(JOptionPane.showInputDialog(frame, "Enter Student ID:"));
                            String deleteSubject = JOptionPane.showInputDialog(frame, "Enter Subject:");
                            departmentHead.deleteMarks(deleteStudentID, deleteSubject);
                            break;
                        default:
                            JOptionPane.showMessageDialog(frame, "Invalid action.");
                    }
                }
            }
        });

        frame.setVisible(true);
    }
    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Update Student Marks");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);

        JPanel panel = new JPanel(new GridLayout(4, 2));
        frame.add(panel);

        JTextField studentIdField = new JTextField();
        JTextField subjectField = new JTextField();
        JTextField marksField = new JTextField();

        panel.add(new JLabel("Student ID:"));
        panel.add(studentIdField);
        panel.add(new JLabel("Subject:"));
        panel.add(subjectField);
        panel.add(new JLabel("Marks:"));
        panel.add(marksField);

        JButton updateButton = new JButton("Update");
        updateButton.addActionListener(e -> {
            int studentId = Integer.parseInt(studentIdField.getText());
            String subject = subjectField.getText();
            int marks = Integer.parseInt(marksField.getText());

            try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/studentmarksmanagement", "root", "");
                 PreparedStatement preparedStatement = connection.prepareStatement(
                         "UPDATE marks_table SET marks = ? WHERE student_id = ? AND subject = ?")) {
                preparedStatement.setInt(1, marks);
                preparedStatement.setInt(2, studentId);
                preparedStatement.setString(3, subject);

                int rowsAffected = preparedStatement.executeUpdate();
                if (rowsAffected > 0) {
                    JOptionPane.showMessageDialog(frame, "Marks updated successfully.");
                } else {
                    JOptionPane.showMessageDialog(frame, "No records updated. Check student ID and subject.");
                }

            } catch (SQLException ex) {
                JOptionPane.showMessageDialog(frame, "Error occurred: " + ex.getMessage());
                ex.printStackTrace();
            }
        });

        panel.add(updateButton);

        frame.setVisible(true);
    }




}

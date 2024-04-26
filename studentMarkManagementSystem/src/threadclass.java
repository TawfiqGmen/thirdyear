public class threadclass implements Runnable {

   static class thread2 implements Runnable{
    public void run(){
        for(int k=1;k<6;k++){
            System.out.println("ths is thread two");
            System.out.println("still in the thread two ");
        }
    }
       

   }

public void run(){
    System.out.println("print numbers from one through ten");

    for(int i = 1;i<11;i++){
        System.out.println(i);
        try{
            Thread.sleep(1000);
        }
       catch(InterruptedException e){
            e.printStackTrace();
        }
    }
}
    public static void main(String[] args) {
       
//        thread.run();
        Thread thread1 = new Thread();
        threadclass tr1 = new threadclass(thread1);
        tr1.start();






        thread thred2 = new thread();
        thread2 tr2 = new thread2(thred2);
        tr2.start();

        


    }
}

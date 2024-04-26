

public class NotifyWait {

public static void main(String[] args) {
threadwait a = new threadwait();
    a.start();
    System.out.println("wait for output");

    try{
        a.wait();
    }catch(InterruptedException e){
        e.printStackTrace();
    }
    System.out.println(a.total);
}

    static class threadwait extends Thread{
        int  total = 0;


        public void run(){
            synchronized(this){
                for(int i=0;i<5;i++){
                    total+=i;
                
                }
               this.notify();
            }
        }
    } 

    
}
package pancaxrzco.apps.fullstack.controllers;


import org.json.JSONArray;
import org.json.JSONObject;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;


@RestController
@RequestMapping("/api/messages")
public class MessageController {

    @GetMapping("/hello")
    public String hello(){
        return "Hello, world!";
    }



    /*
    * Returns string representation of
    * JSONArray[
    *   JSONObject (chart):
    *       header1: JSONArray[data]
    *       header2: JSONArray[data]
    *       header...: JSONArray[data]
    *       headern-1: JSONArray[data]
    *       headern: JSONArray[data]
    * ]
    * */
    @GetMapping("/getStockCharts")
    public String getStockCharts(){
        JSONArray arr = new JSONArray();
        File f = new File("py_scripts/data_analyze/finalgraphs/");

        File[] kids = f.listFiles();
        for(File chart: kids){
            JSONObject thisChart = new JSONObject();
            try {
                Scanner sc = new Scanner(chart);
                String bigString = "";
                while(sc.hasNextLine()){
                    bigString+=sc.nextLine()+"\n";
                }
                String[] lines = bigString.split("\n+");
                String[] headers = lines[0].split(",");
                //System.out.println(Arrays.toString(headers));
                JSONArray[] headerObjs = new JSONArray[headers.length];
                thisChart.put("chart_name",chart.getName().replace("$","").replace("_hist.csv",""));
                for(int i=0;i<headers.length;i++){
                    headerObjs[i]=new JSONArray();
                    thisChart.put(headers[i],headerObjs[i]);
                }
                for(int i=1;i<lines.length;i++){
                    String[] data = lines[i].split(",");
                    for(int j=0;j<data.length;j++){
                        headerObjs[j].put(data[j]);
                    }
                }



            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
            arr.put(thisChart);
        }
        return arr.toString();
    }

    @GetMapping("/getPredictions")
    public String getPredictions(){
        JSONArray returnArr = new JSONArray();

        File f = new File("py_scripts/data_analyze/predictions/");
        File[] files = f.listFiles();

        File importantFile=null;
        for(File x: files){
            if(x.getName().contains(".txt")){
                importantFile=x;
                break;
            }

        }

        HashMap<String,String> names = new HashMap<>();
        HashMap<String,File> namesToFiles = new HashMap<String, File>();
        try {

            Scanner sc = new Scanner(importantFile);
            String bigString="";
            while(sc.hasNextLine()){
                bigString+=sc.nextLine()+"\n";
            }

            String[] lines = bigString.split("\n");
            for(String line:lines){
                String[] splitter = line.split(",");
                String[] splitAgain = splitter[1].split(": ");

                names.put(splitter[0],splitAgain[1]);
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        for(String x: names.keySet()){
            for(File file: files){

                if(file.getName().equals(x+".png")){
                    System.out.println("equals");
                    namesToFiles.put(x,file);
                }
            }
        }



        //in names is name and r value
        //in namestofiles is name and png file

        for(String x:names.keySet()){

            JSONObject object = new JSONObject();
            object.put("name",x);
            object.put("r_value",names.get(x));
            object.put("image_url",namesToFiles.get(x).getAbsolutePath());
            returnArr.put(object);
        }


        return returnArr.toString();
    }
}

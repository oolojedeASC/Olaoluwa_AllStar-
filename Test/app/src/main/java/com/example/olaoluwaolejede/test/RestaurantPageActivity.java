package com.example.olaoluwaolejede.test;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class RestaurantPageActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_restaurant_page);

        final Button BigBtn = (Button) findViewById(R.id.restselBtn);

        BigBtn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                //contBtn.setText("Clicked");
                Intent intent = new Intent(RestaurantPageActivity.this, RestaurantInfoActivity.class);
                RestaurantPageActivity.this.startActivity(intent);
            }

        });

    }
}
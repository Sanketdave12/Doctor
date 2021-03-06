import React from "react";

const Counter = () => {
  return (
    <div>
      <section class="counter">
        <div class="container container-custom">
          <div class="row">
            <div class="col-sm-4 col-md-3 col-lg-3">
              <div class="counter-block">
                <img src="/static/images/counter1.png" alt="#" />
                <div class="counter-text">
                  <h2>60+</h2>
                  <p>Expert Doctors</p>
                </div>
              </div>
            </div>
            <div class="col-sm-4 col-md-3 col-lg-3">
              <div class="counter-block">
                <img src="/static/images/counter2.png" alt="#" />
                <div class="counter-text">
                  <h2>1000+</h2>
                  <p>Happy Patients</p>
                </div>
              </div>
            </div>
            <div class="col-sm-4 col-md-3 col-lg-3">
              <div class="counter-block">
                <img src="/static/images/counter3.png" alt="#" />
                <div class="counter-text">
                  <h2>150+</h2>
                  <p>Award Winner</p>
                </div>
              </div>
            </div>
            <div class="col-sm-12 col-md-3 col-lg-3 d-flex align-items-center justify-content-end">
              <div class="counter-btn_block">
                <a href="#" class="btn btn-success">
                  BOOK NOW
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Counter;

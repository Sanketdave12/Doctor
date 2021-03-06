import React from "react";

const Error = () => {
  return (
    <div>
      <section class="error d-flex align-items-center">
        <div class="container">
          <div class="row justify-content-center align-items-center">
            <div class="col-md-8">
              <div class="error-box">
                <h1>404</h1>
                <h2>Uh-Oh...Page not found!</h2>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                  Aliquam non ante vel velit viverra laoreet. Curabitur
                  vestibulum venenatis massa at mollis.{" "}
                </p>
                <a href="index.html" class="btn btn-dark">
                  HOMEPAGE
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Error;

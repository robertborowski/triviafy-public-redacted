class FooterNotSignedInClass extends HTMLElement {  
  constructor() {
    super();

    // print the variable passed in
    // console.log(this.getAttribute("link_home"));
  }

  connectedCallback() {
    this.innerHTML = `
    <footer class="footer-not-signed-in">
      <div class="footer-not-signed-in-background">
        <div class="footer-not-signed-in-links">
          <ul>
            <li><a href="${this.getAttribute("link_home_js")}">Home</a></li>
            <li><a href="${this.getAttribute("link_about_js")}">About</a></li>
            <li><a href="${this.getAttribute("link_privacy_js")}">Privacy</a></li>
          </ul>
        </div>
        <div class="footer-not-signed-in-copyright">
          <p>Copyright © 2021 Triviafy.</p>
          <p>All rights reserved.</p>
        </div>
      </div>
    </footer>
    `;
  }
}

customElements.define('footer-not-signed-in-component', FooterNotSignedInClass);
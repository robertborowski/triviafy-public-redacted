class CompanyNameChannelClass extends HTMLElement {  
  constructor() {
    super();

    // print the variable passed in
    // console.log(this.getAttribute("link_home"));
  }

  connectedCallback() {
    this.innerHTML = `
    <div class="client-company-and-channel-names">
      <p class="client-free-trial-period">Free Trial Ends: ${this.getAttribute("free_trial_end_date_js")}, ${this.getAttribute("free_trial_days_left_js")} days left.</p>
      <p class="client-company-name">${this.getAttribute("company_name_js")}</p>
      <p class="client-channel-name">${this.getAttribute("channel_name_js")}</p>
    </div>
    `;
  }
}

customElements.define('company-name-channel-component', CompanyNameChannelClass);
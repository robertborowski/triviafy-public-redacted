class CompanyNameChannelClass extends HTMLElement {  
  constructor() {
    super();

    // print the variable passed in
    // console.log(this.getAttribute("link_home"));
  }

  connectedCallback() {
    this.innerHTML = `
    <div class="client-company-and-channel-names">
      <p class="client-free-trial-period">${this.getAttribute("free_trial_ends_info_js")}</p>
      <p class="client-company-name">${this.getAttribute("company_name_js")}</p>
      <p class="client-channel-name">${this.getAttribute("channel_name_js")}</p>
    </div>
    `;
  }
}

customElements.define('company-name-channel-component', CompanyNameChannelClass);
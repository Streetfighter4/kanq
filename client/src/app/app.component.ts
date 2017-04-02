import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <navbar></navbar>
    <h1>Hello {{name}}</h1>
    <form action="/oauth/facebook/authorize" method="GET">
      <input type="submit" value="Facebook login">
    </form>
    <router-outlet></router-outlet>
  `,
})
export class AppComponent  {
  name = 'Kanq';
}

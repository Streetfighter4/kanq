import { Component } from '@angular/core';

@Component({
  selector: 'my-app',
  template: `
    <h1>Hello {{name}}</h1>
    <form action="/oauth/facebook/authorize" method="GET">
      <input type="submit" value="Facebook login">
    </form>
    <form action="/oauth/deviant_art/authorize" method="GET">
      <input type="submit" value="Deviant art login">
    </form>
    <router-outlet></router-outlet>
  `,
})
export class AppComponent  {
  name = 'Kanq';
}

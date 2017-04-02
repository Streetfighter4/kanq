import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <navbar></navbar>
    <h1>Hello {{name}}</h1>
    <form action="/oauth/facebook/authorize" method="GET">
      <button type="submit" class="btn btn-primary">Facebook login</button>
    </form>
    <router-outlet></router-outlet>
  `,
})
export class AppComponent  {
  name = 'Kanq';
}

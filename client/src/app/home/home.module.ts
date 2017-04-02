import {NgModule} from '@angular/core';
import {HomeComponent} from './home.component';
import {RouterModule} from '@angular/router';

@NgModule({
  imports: [
    RouterModule.forRoot([
      {path: 'home', component: HomeComponent}
    ])
  ],
  declarations: [
    HomeComponent,
  ],
  exports: [
    HomeComponent
  ]
})
export class HomeModule {}

import {RouterModule, Routes} from '@angular/router';
import {FacebookAuthorizerComponent} from './oauth/facebook/facebook_authorizer.component';
import {NgModule} from '@angular/core';
import {FacebookTokenComponent} from './oauth/facebook/facebook_token.component';

const routes: Routes = [
  {path: 'oauth/facebook/authorize', component: FacebookAuthorizerComponent},
  {path: 'oauth/facebook/token', component: FacebookTokenComponent}
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}

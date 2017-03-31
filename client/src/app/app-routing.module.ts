import {RouterModule, Routes} from '@angular/router';
import {FacebookAuthorizerComponent} from './oauth/facebook/facebook_authorizer.component';
import {FacebookAuthenticatorComponent} from './oauth/facebook/facebook_authenticator.component';
import {NgModule} from '@angular/core';

const routes: Routes = [
  {path: 'oauth/facebook/authorize', component: FacebookAuthorizerComponent},
  {path: 'oauth/facebook/authenticate', component: FacebookAuthenticatorComponent}
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}

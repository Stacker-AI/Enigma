import { Component } from '@angular/core';
import { EnigmaServiceService } from 'src/services/enigma-service.service';
import { Enigma } from '../Models/Enigma';

@Component({
  selector: 'app-enigma-dash-board',
  templateUrl: './enigma-dash-board.component.html',
  styleUrls: ['./enigma-dash-board.component.css']
})
export class EnigmaDashBoardComponent {

    userInput:Enigma={};

    

constructor(private enigmaSer:EnigmaServiceService){
         
}




  submitPrompt()
  {
     this.enigmaSer.sendPrompt(this.userInput).subscribe(
      response=>{
        console.log('response from server : ',response);
      },
      
      error => {
        console.error('Error sending data to server:', error);
        // Handle error
      }
     )
  }

}

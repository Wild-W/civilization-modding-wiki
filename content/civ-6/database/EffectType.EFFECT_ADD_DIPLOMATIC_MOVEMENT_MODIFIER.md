---
tags:
- EffectType
title: EFFECT_ADD_DIPLOMATIC_MOVEMENT_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_DIPLOMATIC_MOVEMENT_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* DiplomaticYieldSource `String`
>		* CITY_CAPTURED>		  LIBERATION>		  LIBERATION_WAR_INITIATED>		  PROTECTORATE_WAR_INITIATED>		  SURPRISE_WAR_INITIATED>		  TERRITORIAL_EXPANSION_WAR_INITIATED>		  WAR_DECLARATION_INITIATED>		  WAR_DECLARATION_RECEIVED
>	* TurnsActive `Integer`

## Samples

```SQL {title="TRAIT_FALLBABYLON_SURPRISE_MOVEMENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FALLBABYLON_SURPRISE_MOVEMENT",
		"MODIFIER_PLAYER_ADD_DIPLOMATIC_MOVEMENT_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FALLBABYLON_SURPRISE_MOVEMENT",
		"Amount",
		2
	),
	(
		"TRAIT_FALLBABYLON_SURPRISE_MOVEMENT",
		"DiplomaticYieldSource",
		"SURPRISE_WAR_INITIATED"
	),
	(
		"TRAIT_FALLBABYLON_SURPRISE_MOVEMENT",
		"TurnsActive",
		10
	);
	
```


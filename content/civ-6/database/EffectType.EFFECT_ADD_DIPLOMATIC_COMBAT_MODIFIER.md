---
tags:
- EffectType
title: EFFECT_ADD_DIPLOMATIC_COMBAT_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_DIPLOMATIC_COMBAT_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* DiplomaticYieldSource `String`
>		* CITY_CAPTURED>		  LIBERATION>		  LIBERATION_WAR_INITIATED>		  PROTECTORATE_WAR_INITIATED>		  SURPRISE_WAR_INITIATED>		  TERRITORIAL_EXPANSION_WAR_INITATED>		  WAR_DECLARATION_INITIATED>		  WAR_DECLARATION_RECEIVED
>	* ReligiousOnly `Boolean`
>	* TurnsActive `Integer`

## Samples

```SQL {title="TRAIT_TERRITORIAL_WAR_COMBAT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_TERRITORIAL_WAR_COMBAT",
		"MODIFIER_PLAYER_ADD_DIPLOMATIC_COMBAT_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_TERRITORIAL_WAR_COMBAT",
		"Amount",
		5
	),
	(
		"TRAIT_TERRITORIAL_WAR_COMBAT",
		"DiplomaticYieldSource",
		"TERRITORIAL_EXPANSION_WAR_INITIATED"
	),
	(
		"TRAIT_TERRITORIAL_WAR_COMBAT",
		"ReligiousOnly",
		0
	),
	(
		"TRAIT_TERRITORIAL_WAR_COMBAT",
		"TurnsActive",
		10
	);
	
```


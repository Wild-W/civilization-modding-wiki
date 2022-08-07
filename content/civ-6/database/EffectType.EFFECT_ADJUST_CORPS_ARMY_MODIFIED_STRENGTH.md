---
tags:
- EffectType
title: EFFECT_ADJUST_CORPS_ARMY_MODIFIED_STRENGTH
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CORPS_ARMY_MODIFIED_STRENGTH
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Corps `Boolean`
>	* Domain `String`
>		* DOMAIN_AIR>		  DOMAIN_LAND>		  DOMAIN_SEA

## Samples
```SQL {title="TRAIT_LAND_CORPS_COMBAT_STRENGTH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_LAND_CORPS_COMBAT_STRENGTH",
		"MODIFIER_PLAYER_CORPS_ARMY_MODIFIED_STRENGTH"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_LAND_CORPS_COMBAT_STRENGTH",
		"Amount",
		5
	),
	(
		"TRAIT_LAND_CORPS_COMBAT_STRENGTH",
		"Corps",
		1
	),
	(
		"TRAIT_LAND_CORPS_COMBAT_STRENGTH",
		"Domain",
		"DOMAIN_LAND"
	);
	
```


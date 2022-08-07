---
tags:
- EffectType
title: EFFECT_TRIGGER_GAME_MECHANIC
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_TRIGGER_GAME_MECHANIC
>
> * Class: `ANY`
> * Parameters:
>	* MechanicName `String`
>		* GenerateLandAntiquities>		  GenerateSeaAntiquities

## Samples
```SQL {title="CIVIC_GENERATE_LAND_ANTIQUITIES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CIVIC_GENERATE_LAND_ANTIQUITIES",
		"MODIFIER_GAME_TRIGGER_MECHANIC"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CIVIC_GENERATE_LAND_ANTIQUITIES",
		"MechanicName",
		"GenerateLandAntiquities"
	);
	
```


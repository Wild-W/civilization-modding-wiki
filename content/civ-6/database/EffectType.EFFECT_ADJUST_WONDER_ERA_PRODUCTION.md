---
tags:
- EffectType
title: EFFECT_ADJUST_WONDER_ERA_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_WONDER_ERA_PRODUCTION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* EndEra `String`
>	* IsWonder `Boolean`
>	* StartEra `String`

## Samples
```SQL {title="MONUMENT_TO_THE_GODS_ANCIENTCLASSICALWONDER_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MONUMENT_TO_THE_GODS_ANCIENTCLASSICALWONDER_MODIFIER",
		"MODIFIER_PLAYER_CITIES_ADJUST_WONDER_ERA_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MONUMENT_TO_THE_GODS_ANCIENTCLASSICALWONDER_MODIFIER",
		"Amount",
		15
	),
	(
		"MONUMENT_TO_THE_GODS_ANCIENTCLASSICALWONDER_MODIFIER",
		"EndEra",
		"ERA_CLASSICAL"
	),
	(
		"MONUMENT_TO_THE_GODS_ANCIENTCLASSICALWONDER_MODIFIER",
		"IsWonder",
		1
	),
	(
		"MONUMENT_TO_THE_GODS_ANCIENTCLASSICALWONDER_MODIFIER",
		"StartEra",
		"ERA_ANCIENT"
	);
	
```


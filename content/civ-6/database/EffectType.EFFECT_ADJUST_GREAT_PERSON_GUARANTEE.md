---
tags:
- EffectType
title: EFFECT_ADJUST_GREAT_PERSON_GUARANTEE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GREAT_PERSON_GUARANTEE
>
> * Class: `PLAYERS`
> * Parameters:
>	* EraType `String`
>		* [GreatPersonClasses.GreatPersonClassType]
>	* GreatPersonClassType `String`
>		* [GreatPersonClasses.GreatPersonClassType]

## Samples

```SQL {title="TRAIT_LEADER_COMANDANTE_GENERAL_GUARANTEE_CLASSICAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_LEADER_COMANDANTE_GENERAL_GUARANTEE_CLASSICAL",
		"MODIFIER_PLAYER_ADJUST_GREAT_PERSON_GUARANTEE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_LEADER_COMANDANTE_GENERAL_GUARANTEE_CLASSICAL",
		"EraType",
		"ERA_CLASSICAL"
	),
	(
		"TRAIT_LEADER_COMANDANTE_GENERAL_GUARANTEE_CLASSICAL",
		"GreatPersonClassType",
		"GREAT_PERSON_CLASS_COMANDANTE_GENERAL"
	);
	
```


```SQL {title="TRAIT_GUARANTEE_ONE_PROPHET"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_GUARANTEE_ONE_PROPHET",
		"MODIFIER_PLAYER_ADJUST_GREAT_PERSON_GUARANTEE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_GUARANTEE_ONE_PROPHET",
		"GreatPersonClassType",
		"GREAT_PERSON_CLASS_PROPHET"
	);
	
```


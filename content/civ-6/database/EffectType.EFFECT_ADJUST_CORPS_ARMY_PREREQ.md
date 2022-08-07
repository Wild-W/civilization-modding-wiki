---
tags:
- EffectType
title: EFFECT_ADJUST_CORPS_ARMY_PREREQ
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CORPS_ARMY_PREREQ
>
> * Class: `PLAYERS`
> * Parameters:
>	* CivicType `String`
>		* [Civics.CivicType]
>	* Corps `Boolean`
>	* Domain `String`
>		* DOMAIN_AIR>		  DOMAIN_LAND>		  DOMAIN_SEA

## Samples

```SQL {title="TRAIT_NAVAL_CORPS_EARLY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_NAVAL_CORPS_EARLY",
		"MODIFIER_PLAYER_CORPS_ARMY_PREREQ"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_NAVAL_CORPS_EARLY",
		"CivicType",
		"CIVIC_MERCANTILISM"
	),
	(
		"TRAIT_NAVAL_CORPS_EARLY",
		"Corps",
		1
	),
	(
		"TRAIT_NAVAL_CORPS_EARLY",
		"Domain",
		"DOMAIN_SEA"
	);
	
```


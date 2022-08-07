---
tags:
- EffectType
title: EFFECT_GRANT_BOOST_WITH_GREAT_PERSON
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_BOOST_WITH_GREAT_PERSON
>
> * Class: `PLAYERS`
> * Parameters:
>	* GreatPersonClass `String`
>		* [GreatPersonClasses.GreatPersonClassType]
>	* OtherPlayers `Boolean`
>	* TechBoost `Boolean`

## Samples

```SQL {title="GREATLIBRARY_BOOST_SCIENTIST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GREATLIBRARY_BOOST_SCIENTIST",
		"MODIFIER_PLAYER_GRANT_BOOST_WITH_GREAT_PERSON"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATLIBRARY_BOOST_SCIENTIST",
		"GreatPersonClass",
		"GREAT_PERSON_CLASS_SCIENTIST"
	),
	(
		"GREATLIBRARY_BOOST_SCIENTIST",
		"OtherPlayers",
		1
	),
	(
		"GREATLIBRARY_BOOST_SCIENTIST",
		"TechBoost",
		1
	);
	
```


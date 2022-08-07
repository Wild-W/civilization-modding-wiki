---
tags:
- EffectType
title: EFFECT_ADD_DIPLOMATIC_ACTION_OVERRIDE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_DIPLOMATIC_ACTION_OVERRIDE
>
> * Class: `PLAYERS`
> * Parameters:
>	* CivicType `String`
>		* [Civics.CivicType]
>	* DiplomaticAction `String`
>		* [DiplomaticActions.DiplomaticActionType]

## Samples

```SQL {title="TRAIT_TERRITORIAL_WAR_PREREQ_OVERRIDE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_TERRITORIAL_WAR_PREREQ_OVERRIDE",
		"MODIFIER_PLAYER_ADD_DIPLOMATIC_ACTION_OVERRIDE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_TERRITORIAL_WAR_PREREQ_OVERRIDE",
		"CivicType",
		"CIVIC_MILITARY_TRAINING"
	),
	(
		"TRAIT_TERRITORIAL_WAR_PREREQ_OVERRIDE",
		"DiplomaticAction",
		"DIPLOACTION_DECLARE_TERRITORIAL_WAR"
	);
	
```


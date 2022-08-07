---
tags:
- EffectType
title: EFFECT_ADJUST_BANNED_DIPLOMATIC_ACTIONS_SPECIFIC_CIVILIZATION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_BANNED_DIPLOMATIC_ACTIONS_SPECIFIC_CIVILIZATION
>
> * Class: `Unknown`
> * Parameters:
>	* CivilizationType `String`
>		* [Civilizations.CivilizationType]
>	* DiplomaticActionType `String`
>		* [DiplomaticActions.DiplomaticActionType]

## Samples

```SQL {title="TRAIT_NO_SUPRISE_WAR_ON_CANADA"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_NO_SUPRISE_WAR_ON_CANADA",
		"MODIFIER_PLAYER_ADJUST_BANNED_DIPLOMATIC_ACTION_SPECIFIC_CIVILIZATION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_NO_SUPRISE_WAR_ON_CANADA",
		"CivilizationType",
		"CIVILIZATION_CANADA"
	),
	(
		"TRAIT_NO_SUPRISE_WAR_ON_CANADA",
		"DiplomaticActionType",
		"DIPLOACTION_DECLARE_SURPRISE_WAR"
	);
	
```


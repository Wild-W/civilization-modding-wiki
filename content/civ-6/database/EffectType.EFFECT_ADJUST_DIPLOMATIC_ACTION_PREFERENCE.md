---
tags:
- EffectType
title: EFFECT_ADJUST_DIPLOMATIC_ACTION_PREFERENCE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DIPLOMATIC_ACTION_PREFERENCE
>
> * Class: `PLAYERS`
> * Parameters:
>	* Action `String`
>	* Favored `Boolean`

## Samples

```SQL {title="TRAIT_BEFRIEND_MINOR_CIV_HOME_CONTINENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TRAIT_BEFRIEND_MINOR_CIV_HOME_CONTINENT",
		"MODIFIER_ADJUST_DIPLOMATIC_ACTION_PREFERENCE",
		"REQUIREMENTS_INDEPT_MINOR_CIV_HOME_CONTINENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_BEFRIEND_MINOR_CIV_HOME_CONTINENT",
		"Action",
		"DIPLOACTION_GRANT_INFLUENCE_TOKEN"
	),
	(
		"TRAIT_BEFRIEND_MINOR_CIV_HOME_CONTINENT",
		"Favored",
		1
	);
	
```

